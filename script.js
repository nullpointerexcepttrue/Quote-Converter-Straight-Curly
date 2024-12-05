document.getElementById('toCurly').addEventListener('click', () => {
  const text = document.getElementById('inputText').value;
  const converted = text
    .replace(/"/g, '“').replace(/"/g, '”')
    .replace(/'/g, '‘').replace(/'/g, '’');
  document.getElementById('outputText').textContent = converted;
});

document.getElementById('toStraight').addEventListener('click', () => {
  const text = document.getElementById('inputText').value;
  const converted = text
    .replace(/“/g, '"').replace(/”/g, '"')
    .replace(/‘/g, "'").replace(/’/g, "'");
  document.getElementById('outputText').textContent = converted;
});
