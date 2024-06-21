document.addEventListener('DOMContentLoaded', () => {
  fetch('main.json')
      .then(response => response.json())
      .then(data => {
        DisplayMovieDetails(data);
      })
      .catch(error => console.error('Error fetching data:', error));
});


function DisplayMovieDetails(movies) {
  const movieContainer = document.getElementById('movie-container');

  movies.forEach(movie => {
    const movieDiv = document.createElement('div');
    movieDiv.classList.add('movie');

    const movieNameDiv = document.createElement('div');
    movieNameDiv.classList.add('movie-name');
    movieNameDiv.innerHTML = `<strong>${escapeHTML(movie.TITLE)}</strong> (${escapeHTML(movie.YEAR)})`;

    const ratingDiv = document.createElement('div');
    ratingDiv.classList.add('rating');
    ratingDiv.innerHTML = getStarRating(parseFloat(movie.RATING), 10);

    movieDiv.appendChild(movieNameDiv);
    movieDiv.appendChild(ratingDiv);

    movieContainer.appendChild(movieDiv);

    // Set background image directly to the movie div
    movieDiv.style.backgroundImage = `url('${movie.ICON}')`;
  });
}



function getStarRating(score, outOf) {
  const fullStar = '★';
  const emptyStar = '☆';
  const fullStars = Math.round(score / outOf * 5);
  const emptyStars = 5 - fullStars;

  return fullStar.repeat(fullStars) + emptyStar.repeat(emptyStars);
}

function escapeHTML(str) {
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}
