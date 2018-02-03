var lebronUrl = "https://img.wennermedia.com/article-leads-horizontal-1400/lebron-james-on-race-trump-retirement-cb1f9039-23c4-478a-83e6-2ded5158068c.jpg";
var host = "https://localhost:3000";
var images = document.getElementsByTagName('img');
replaceImages(images, lebronUrl);

function replaceImages(images, imageUrl) {
    for (var i = 0, l = images.length; i < l; i++) {
	fetchUpdatedImage(images[i].src)
        images[i].src = imageUrl;
    }
}

function fetchUpdatedImage(imageUrl) {
    var uri = encodeURI(imageUrl);
    console.log("uri: " + uri);

    var xhr = new XMLHttpRequest();

    console.log("attempted host: " + host + "/process?url=" + uri);
    xhr.open("GET", host + "/process?url=" + uri, false);
    xhr.send();

    var result = xhr.responseText;
    console.log("Response: " + result);
}
