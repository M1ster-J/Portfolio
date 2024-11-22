 // Initialize Leaflet map
 const map = L.map('map').setView([0, 0], 2); // Default to world view
 const radarLayer = L.tileLayer(
     'https://tilecache.rainviewer.com/v2/radar/256/{z}/{x}/{y}/2/0_0.png',
     { attribution: 'RainViewer.com' }
 ).addTo(map);

 // Geocoding with OpenStreetMap (no API key required)
 function searchLocation() {
     const location = document.getElementById('locationSearch').value;
     fetch(`https://nominatim.openstreetmap.org/search?q=${location}&format=json`)
         .then(response => response.json())
         .then(data => {
             if (data.length > 0) {
                 const { lat, lon } = data[0]; // Use first result
                 map.setView([lat, lon], 10); // Center map and set zoom
             } else {
                 alert('Location not found. Please try another search.');
             }
         })
         .catch(error => console.error('Error with geocoding:', error));
 }