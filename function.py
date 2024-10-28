def get_device_info(make, model, id_model):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }

    model_name_for_url = model.replace(" ", "_").lower()  
    make_lower = make.lower()  
    search_url = f'https://www.gsmarena.com/{make_lower}_{model_name_for_url}-{id_model}.php'
    
    print(f"Fetching from: {search_url}")  
    response = requests.get(search_url, headers=headers)

    if response.status_code != 200:
        print("Failed to fetch device details")
        return None

    soup = BeautifulSoup(response.text, 'lxml')

    # Inspect the structure of the detail page
    try:
        model_name = soup.find('h1', {'class': "specs-phone-name-title"}).text.strip()
        dimensions = soup.find('td', {'data-spec': "dimensions"})
        dimensions_text = dimensions.text.strip() if dimensions else "Not found"
        
        display_size = soup.find('td', {'data-spec': "displaysize"})
        display_size_text = display_size.text.strip() if display_size else "Not found"
        
        display_resolution = soup.find('td', {'data-spec': "displayresolution"})
        display_resolution_text = display_resolution.text.strip() if display_resolution else "Not found"
        
        cpu = soup.find('td', {'data-spec': "cpu"})
        cpu_text = cpu.text.strip() if cpu else "Not found"
        
        gpu = soup.find('td', {'data-spec': "gpu"})
        gpu_text = gpu.text.strip() if gpu else "Not found"
        
        memory = soup.find('td', {'data-spec': "internalmemory"})
        memory_text = memory.text.strip() if memory else "Not found"
        
        price = soup.find('td', {'data-spec': "price"})
        price_text = price.text.replace('\u2009', "").strip() if price else "Not found"
        
        return {
            "make": make,
            "model": model,
            "model_name": model_name,
            "dimensions": dimensions_text,
            "display_size": display_size_text,
            "display_resolution": display_resolution_text,
            "cpu": cpu_text,
            "gpu": gpu_text,
            "memory": memory_text,
            "price": price_text
        }
    except Exception as e:
        print(f"Error extracting details for {make} {model}: {e}")  
        return None