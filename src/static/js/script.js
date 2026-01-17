const pdfForm = document.getElementById("pdf-form");
const fileInput = document.getElementById("input-pdf-file");
const fileNameSpan = document.getElementById("file-name");

pdfForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  if (fileInput.files.length === 0) {
    fileNameSpan.textContent =
      "Por favor, selecione um arquivo PDF antes de enviar.";
    fileNameSpan.style.color = "red";
    return;
  }

  const formData = new FormData(pdfForm);

  document.getElementById("result-classification").textContent =
    "Classificando...";
  document.getElementById("result-reason").textContent = "Buscando motivo...";
  document.getElementById("result-suggestion").textContent = "Buscando sugestão...";

  const response = await fetch("http://127.0.0.1:8000/upload", {
    method: "POST",
    body: formData,
  });

  const data = await response.json();

  renderResult(data.response);
});

fileInput.addEventListener("change", () => {
  fileNameSpan.style.color = "#555";

  if (fileInput.files.length > 0) {
    fileNameSpan.textContent = fileInput.files[0].name;
  } else {
    fileNameSpan.textContent = "Nenhum arquivo selecionado";
  }
});

function renderResult(result) {
  document.getElementById("result-classification").textContent =
    result.classification;

  document.getElementById("result-reason").textContent = result.reason;

  document.getElementById("result-suggestion").textContent =
    result.suggested_response;
}
