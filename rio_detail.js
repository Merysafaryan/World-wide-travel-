document.addEventListener("DOMContentLoaded", function () {
    const detailsBtnRio = document.getElementById("details-btn-rio");
    const detailsContainerRio = document.getElementById("rio-details");

    if (detailsBtnRio) {
        detailsBtnRio.addEventListener("click", function () {
            const content = `
                <h4>Best Places to Visit</h4>
                <ul>
                    <li><strong>Christ the Redeemer:</strong> One of the Seven Wonders of the Modern World.</li>
                    <li><strong>Sugarloaf Mountain:</strong> Iconic views of the city and coastline.</li>
                    <li><strong>Copacabana Beach:</strong> Famous beach with lively atmosphere and scenic views.</li>
                    <li><strong>Lapa Arches:</strong> Historic arches and vibrant nightlife district.</li>
                </ul>
                <h4>Best Time to Visit</h4>
                <p>The best time to visit Rio is during the summer months (December to March), with sunny weather and lively carnival festivities.</p>
            `;
        });
    }
});
