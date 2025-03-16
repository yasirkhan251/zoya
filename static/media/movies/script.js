document.getElementById("uploadForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission

    var formData = new FormData(this);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", this.action, true);

    xhr.upload.onprogress = function(event) {
        var percent = (event.loaded / event.total) * 100;
        document.getElementById("progress").style.display = "block";
        document.getElementById("overallProgressBar").style.width = percent + "%";
        document.getElementById("overallProgressText").innerText = percent.toFixed(2) + "% uploaded";
    };

    xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            if (xhr.status == 200) {
                window.location.href = "/drive/movies/";
            } else {
                alert("Error uploading files.");
            }
        }
    };

    xhr.send(formData);
});

document.getElementById('showFormBtn').addEventListener('click', function() {
    document.getElementById('hiddenForm').classList.add('visible');
});

window.onload = function() {
    var defaultThumbnail = 'https://cdn1.vectorstock.com/i/1000x1000/18/30/music-icon-white-on-the-blue-background-vector-3451830.jpg';

    var audioElements = document.querySelectorAll('audio');

    audioElements.forEach(function(audio) {
        var src = audio.getAttribute('src');

        var thumbnail = document.createElement('img');
        thumbnail.alt = src;
        thumbnail.className = 'thumbnail';

        var canvas = document.createElement('canvas');
        var context = canvas.getContext('2d');
        canvas.width = 100; // Thumbnail width
        canvas.height = 100; // Thumbnail height

        var audioObj = new Audio();
        audioObj.src = src;
        audioObj.preload = 'metadata';

        audioObj.onloadedmetadata = function() {
            try {
                context.drawImage(audioObj, 0, 0, canvas.width, canvas.height);
                thumbnail.src = canvas.toDataURL('image/png');
            } catch (error) {
                console.error('Error generating thumbnail:', error);
                thumbnail.src = defaultThumbnail;
            }
            audio.parentNode.insertBefore(thumbnail, audio.nextSibling);
        };

        audioObj.onerror = function(error) {
            console.error('Error loading audio:', error);
            thumbnail.src = defaultThumbnail;
            audio.parentNode.insertBefore(thumbnail, audio.nextSibling);
        };

        audio.addEventListener('play', function() {
            pauseAllOthers(audio);
        });
    });

    function pauseAllOthers(currentAudio) {
        audioElements.forEach(function(audio) {
            if (audio !== currentAudio) {
                audio.pause();
            }
        });
    }
};
function searchSongs() {
    var input, filter, container, songs, songTitles, i, txtValue;
    input = document.getElementById('searchInput');
    filter = input.value.toUpperCase();
    container = document.getElementById("songContainer");
    songs = container.getElementsByClassName('song-item');

    for (i = 0; i < songs.length; i++) {
        songTitles = songs[i].getElementsByClassName("heading_section");
        txtValue = songTitles[0].textContent || songTitles[0].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            songs[i].style.display = "";
        } else {
            songs[i].style.display = "none";
        }
    }
}
