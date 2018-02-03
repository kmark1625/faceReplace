var lebronUrl = "https://img.wennermedia.com/article-leads-horizontal-1400/lebron-james-on-race-trump-retirement-cb1f9039-23c4-478a-83e6-2ded5158068c.jpg";
var images = document.getElementsByTagName('img');
replaceImages(images, lebronUrl);

function replaceImages(images, imageUrl) {
    for (var i = 0, l = images.length; i < l; i++) {
        images[i].src = imageUrl;
    }
}

function fetchUpdatedImage(imageUrl) {
    var xhr = new XMLHttpRequest();
}
