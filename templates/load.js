function updateActivityLog() {
            fetch('/activity')
                .then(response => response.json())
                .then(data => {
                    const activityLog = document.getElementById("activityLog");
                    activityLog.innerHTML = ""; // Clear the existing content
                    data.forEach(filename => {
                        const img = document.createElement("img");
                        img.src = '/screenshots/' + filename;
                        img.alt = "Screenshot";
                        activityLog.appendChild(img);
                    });
                })
                .catch(error => console.error(error));
        }

        // Call updateActivityLog every 5 seconds
        setInterval(updateActivityLog, 5000);
