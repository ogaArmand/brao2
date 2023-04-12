let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 5.332550116063081, lng: -4.055595138128719 },
    zoom: 15,
  });
  var directionsService = new google.maps.DirectionsService;
  var directionsDisplay = new google.maps.DirectionsRenderer({
      map: map
  });

    var waypts = [
        {location: new google.maps.LatLng(5.325753916386461,-4.047817351425592), stopover: true},//Shalom
        {location: new google.maps.LatLng(5.3263053174681865, -4.045769726353335), stopover: true},//Eliel
        {location: new google.maps.LatLng(5.322162340952686, -4.052329074242083), stopover: true}//peniel
    ];
    //{LatLng(5.325753916386461,-4.047817351425592), stopover: true}5.3263053174681865, -4.045769726353335
    //5.322162340952686, -4.052329074242083 peniel

  directionsService.route({
      origin: {lat: 5.334857169298532, lng: -4.045328470316621}, // AD Morija
      waypoints: waypts,
      destination: {lat: 5.337972906801648, lng: -4.05493928386365}, // Emmaüs
      optimizeWaypoints: true,
      travelMode: 'DRIVING'
  }, function(response, status) {
      if (status === 'OK') {
          directionsDisplay.setDirections(response);
      } else {
          window.alert('Directions request failed due to ' + status);
      }
  });

  var marker = new google.maps.Marker({
    position: {lat: 5.334857169298532, lng: -4.045328470316621},
    map: map,
    title: 'Eglise Assemblée de Dieu Temple MORIJA'
});
var infowindow = new google.maps.InfoWindow({
    content: '<h3>MORIJA</h3><p>Le lieu du sacrifice</p>'
});
marker.addListener('click', function() {
    infowindow.open(map, marker);
});
}

window.initMap = initMap;