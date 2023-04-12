function initMap() {
    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 5.332550116063081, lng: -4.055595138128719}, // Morija
        zoom: 15,
    });
    directionsDisplay.setMap(map);

    // Récupération des données depuis Django
    var locations = JSON.parse('{{ locations | safe }}');

    // Ajout des marqueurs et des infowindows
    var infowindows = [];
    for (var i = 0; i < locations.length; i++) {
        var loc = locations[i];
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(loc.lat, loc.lng),
            map: map,
            title: loc.nom
        });
        var infowindow = new google.maps.InfoWindow({
            content: loc.nom
        });
        marker.addListener('click', function () {
            // Fermeture des autres infowindows avant d'afficher celle-ci
            for (var j = 0; j < infowindows.length; j++) {
                infowindows[j].close();
            }
            infowindow.open(map, marker);
        });
        infowindows.push(infowindow);
    }

    // Création des waypoints pour chaque emplacement
    var waypoints = [];
    for (var i = 1; i < locations.length - 1; i++) {
        var loc = locations[i];
        waypoints.push({
            location: new google.maps.LatLng(loc.lat, loc.lng),
            stopover: false
        });
    }

    // Calcul de l'itinéraire
    directionsService.route({
        origin: new google.maps.LatLng(locations[0].lat, locations[0].lng), // Point de départ
        destination: new google.maps.LatLng(locations[locations.length - 1].lat, locations[locations.length - 1].lng), // Point d'arrivée
        waypoints: waypoints,
        optimizeWaypoints: true,
        travelMode: 'DRIVING'
    }, function (response, status) {
        if (status === 'OK') {
            directionsDisplay.setDirections(response);
        } else {
            window.alert('Directions request failed due to ' + status);
        }
    });
}

window.initMap = initMap;