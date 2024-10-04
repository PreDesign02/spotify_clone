async function fetchMusic() {
    const response = await fetch('http://localhost:8000/api/songs/');
    const songs = await response.json();

    const container = document.getElementById('music-container');

    songs.forEach(song => {
        const songElement = document.createElement('div');
        songElement.innerText = song.title;
        container.appendChild(songElement);
    });
}

fetchMusic();