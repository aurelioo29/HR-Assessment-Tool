// form handler
document
  .getElementById("predictionForm")
  .addEventListener("submit", function (e) {
    const inputs = document.querySelectorAll("input");
    let valid = true;

    inputs.forEach((input) => {
      if (!input.value) {
        valid = false;
      }
    });

    if (!valid) {
      e.preventDefault();
      alert("Mohon lengkapi semua field sebelum submit.");
    }
  });

// Predict button handler
document.getElementById("predictButton").addEventListener("click", function () {
  const formData = new FormData(document.getElementById("predictionForm"));

  fetch("/", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.prediction_text) {
        if (data.prediction_text === "STAYED") {
          document.getElementById(
            "result-text"
          ).innerHTML = `<span class="text-success fw-bold">${data.prediction_text}</span>`;
        } else {
          document.getElementById(
            "result-text"
          ).innerHTML = `<span class="text-danger fw-bold">${data.prediction_text}</span>`;
        }

        // Accurate prediction text
        document.getElementById(
          "probability"
        ).innerHTML = `With Accuracy <span class="text-md-end fw-bold">89.53%</span>`;

        const resultContainer = document.getElementById("predictionResult");

        // Clear previous results
        resultContainer.innerHTML = "";

        // Display input results
        for (let key in data.input_data) {
          const resultItem = document.createElement("div");
          resultItem.classList.add("result-item"); // Add class for styling
          resultItem.innerHTML = `<span class="key">${key}:</span> <span class="value">${data.input_data[key]}</span>`;
          resultContainer.appendChild(resultItem);
        }

        const classificationReport = `
        <br />
        <h2>Classification Report:</h2>
        <table>
          <thead>
            <tr>
              <th></th>
              <th>Precision</th>
              <th>Recall</th>
              <th>F1-Score</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Stayed (False)</td>
              <td>0.91</td>
              <td>0.98</td>
              <td>0.94</td>
            </tr>
            <tr>
              <td>Leaves (True)</td>
              <td>0.72</td>
              <td>0.33</td>
              <td>0.46</td>
            </tr>
            <tr>
              <td>Accuracy</td>
              <td colspan="3" style="text-align: center;">0.90</td>
            </tr>
          </tbody>
        </table>
      `;

        resultContainer.innerHTML += classificationReport;
      } else {
        alert("Harap isi data pada setiap form dengan Valid !!!");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("Terjadi kesalahan saat melakukan prediksi.");
    });
});

// reload page handler
window.addEventListener("beforeunload", function (event) {
  const confirmationMessage = "Apakah Anda yakin reload halaman ini? ";

  event.returnValue = confirmationMessage;
  return confirmationMessage;
});

// button reset form
document.getElementById("resetButton").addEventListener("click", function () {
  const confirmReset = window.confirm(
    "Are you sure you want to reset the form and delete the prediction results?"
  );
  if (confirmReset) {
    document.getElementById("predictionForm").reset();

    document.getElementById("result-text").innerHTML = "";
    document.getElementById("probability").innerHTML = "";
    document.getElementById("predictionResult").innerHTML = "";

    document.getElementById("app").scrollIntoView({ behavior: "smooth" });
  } else {
    console.log("Cancel reset form");
  }
});
