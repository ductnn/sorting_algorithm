let values = [];
let w = 10;
let states = [];

function setup() {
  createCanvas(windowWidth, windowHeight);

  values = new Array(floor(width / w));

  for (let i = 0; i < values.length; i++) {
    values[i] = random(height);
    states[i] = -1;
  }

  quickSort(values, 0, values.length - 1);
}

async function quickSort(arr, start, end) {
  if (start >= end) {
    return;
  }
  let index = await partition(arr, start, end);
  states[index] = -1;

  await Promise.all([
    quickSort(arr, start, index - 1),
    quickSort(arr, index + 1, end)
  ]);
}

async function partition(arr, start, end) {
  for (let i = start; i < end; i++) {
    states[i] = 1;
  }

  let pivValue = arr[end];
  let pivIdx = start;
  states[pivIdx] = 0;

  for (let i = start; i < end; i++) {
    if (arr[i] < pivValue) {
      await swap(arr, i, pivIdx);
      states[pivIdx] = -1;
      pivIdx++;
      states[pivIdx] = 0;
    }
  }
  await swap(arr, pivIdx, end);

  for (let i = start; i < end; i++) {
    if (i != pivIdx) {
      states[i] = -1;
    }
  }

  return pivIdx;
}

function draw() {
  background(0);

  for (let i = 0; i < values.length; i++) {
    noStroke();
    if (states[i] == 0) {
      fill('#db141f');
    } else if (states[i] == 1) {
      fill('#0ad10e');
    } else {
      fill(255);
    }
    rect(i * 11, height - values[i], w, values[i]);
  }
}

async function swap(arr, i, j) {
  await sleep(50);
  let temp = arr[i];
  arr[i] = arr[j];
  arr[j] = temp;
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
