const $playedWords = document.querySelector("#words");
const $form = document.querySelector("#newWordForm");
const $wordInput = document.querySelector("#wordInput");
const $message = document.querySelector(".msg");
const $table = document.querySelector("table");

let gameId;

const BOGGLE_GAME_SIZE = 5;

/** Start */

async function start() {
  const response = await fetch(`/api/new-game`, {
    method: "POST",
  });
  const gameData = await response.json();

  gameId = gameData.gameId;
  const board = gameData.board;

  displayBoard(board);
}


/** Display board */

function displayBoard(board) {

  $table.innerHTML = '';

  for (let y = 0; y < BOGGLE_GAME_SIZE; y++) {
    const $tr = document.createElement("tr");
    for (let x = 0; x < BOGGLE_GAME_SIZE; x++) {
      const $td = document.createElement("td");

      $td.setAttribute("x-idx", x.toString());
      $td.setAttribute("y-idx", y.toString());
      $td.innerText = board[y][x];

      $tr.appendChild($td);
    }
    $table.appendChild($tr);
  }
}




/** Handle form submit
 *
 *  - submits word to API
 *  - displays outcome in DOM
 */

async function handleFormSubmit(evt) {
  // TODO
}


// TODO: add an event listener for the form submission

document.addEventListener(click);

/** Submit word to API and return result from the response. */

async function submitWordToAPI(word) {
  // TODO
}


/** Display outcome in DOM based on result of submitting word to API
 *
 * not-word:
 *  - shows an invalid word message
 *
 * not-on-board:
 *  - shows a not on board message
 *
 * ok:
 *  - shows a success message
 *  - adds word to the played words list
 */

function displayOutcome(result, word) {
  // TODO
}


export { start };
