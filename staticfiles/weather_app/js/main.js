$(document).ready(function () {
    $("#city").on("input", function () {
        const query = $(this).val().trim();
        if (query.length >= 3) {
            $.ajax({
                url: `https://nominatim.openstreetmap.org/search`,
                data: {
                    q: query,
                    format: "json",
                    addressdetails: 1,
                    limit: 5,
                },
                dataType: "json",
                headers: {
                    "User-Agent": "weather-app", 
                },
                success: function (data) {
                    const suggestionBox = $('#suggestions');
                    suggestionBox.empty().show();

                    if (data.length > 0) {
                        data.forEach((item) => {
                            const cityName = item.display_name;
                            const suggestion = $(`<li class='list-group-item'>`).text(cityName);
                            suggestion.on("click", function () {
                                $("#city").val(cityName);
                                suggestionBox.hide();
                            });
                            suggestionBox.append(suggestion);
                        });
                    } else {
                        suggestionBox.hide();
                    }
                },
                error: function () {
                    console.error("Error fetching suggestions.");
                    $('#suggestions').hide();
                },
            });
        } else {
            $('#suggestions').hide();
        }
    });
    $(document).on("click", function (e) {
        if (!$(e.target).closest("#suggestions, #city").length) {
            $("#suggestions").hide();
        }
    });
});
