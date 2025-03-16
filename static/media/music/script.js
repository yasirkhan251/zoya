
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
                window.location.href = "/drive/files/music/";
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
