// const dots = document.querySelectorAll('.dot');
// const cardContainer = document.querySelector('.card-container');

// dots.forEach((dot, index) => {
//       dot.addEventListener('click', (event) => {
//             const cardIndex = event.target.dataset.index; // Get the index of the clicked dot
//             const newPosition = cardIndex * -100; // Calculate the new position for the card container

//             cardContainer.style.animation = 'none'; // Disable animation temporarily
//             setTimeout(() => {
//                   cardContainer.style.animation = 'moveCards 120s linear infinite'; // Re-enable animation
//             }, 50);

//             cardContainer.style.transform = `translateX(${newPosition}%)`; // Move the card container to the new position
//             setActiveDot(cardIndex); // Set the active dot
//       });
// });

// function setActiveDot(index) {
//       dots.forEach((dot, i) => {
//             dot.classList.toggle('active', i == index); // Use loose equality to match the index
//       });
// }
