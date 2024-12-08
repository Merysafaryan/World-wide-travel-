document.addEventListener("DOMContentLoaded", function () {
    const detailsBtn = document.getElementById("details-btn-maldives");
    const detailsContainer = document.getElementById("maldives-details");

    if (detailsBtn) {
        detailsBtn.addEventListener("click", function () {
            const content = `
                <h4>Best Places to Visit</h4>
                <ul>
                    <li><strong>Malé:</strong> The capital city with historical sites like the Maldives Islamic Centre.</li>
                    <li><strong>Banana Reef:</strong> Famous for its vibrant coral reefs and diving opportunities.</li>
                    <li><strong>Addu Atoll:</strong> A serene and less touristy area for those seeking tranquility.</li>
                    <li><strong>Maafushi Island:</strong> A local island with an authentic Maldivian experience.</li>
                </ul>
                <h4>Best Time to Visit</h4>
                <p>The ideal time to visit the Maldives is from November to April, when the weather is sunny and dry. The monsoon season from May to October brings more rain but fewer crowds.</p>
            `;
            detailsContainer.innerHTML = content;
        });
    }
});
