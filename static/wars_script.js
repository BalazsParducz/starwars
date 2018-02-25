

// var residents = document.getElementById("residents");

// residents.addEventListener('onclick', )


function getResidentData(){

    var residents = $("#residents").val();
    // residents = residents.replace(/ /g, "")
    debugger;

    for (let resident of JSON.parse(residents).residents) {
        debugger;

        $.ajax({
            dataType: "json",
            type: "GET",
            url: resident,
            success: function (response) {
                console.log(response['name'])
                console.log(response['height'])
                console.log(response['mass'])
                console.log(response['skin_color'])
                console.log(response['hair_color'])
                console.log(response['eye_color'])
                console.log(response['birth_year'])
                console.log(response['gender'])

            }

        });
    }


}


$(function () {
    $("#residents").click(function(){
        var residents= $("#residents").val();
        return residents;
    });
})


function appendToElement(elementToExtend, textToAppend) {
    let fakeDiv = document.createElement("div");
    fakeDiv.innerHTML=textToAppend.trim();
    elementToExtend.appendChild(fakeDiv.firstChild);
    return elementToExtend.lastChild;
}


$(document).ready(function () {
    for (let button of document.getElementsByClassName("residents")) {
        button.addEventListener('click', function () {
            var residentsModal = document.getElementById("residentsModal");
            residentsModal.innerHTML = '';
            var url = JSON.parse(button.getAttribute("value"));
            for (let dataFromUrl of url ) {
                $.ajax({
                    dataType: "json",
                    type: "GET",
                    url: dataFromUrl,
                    success: function (response) {
                        appendToElement(document.getElementById("residentsModal"), modal)
                    }
                });
            };
    });


// Generate modal
var modal = `
          <tbody>
          <tr>
            <td>` + response['name'] + `</td>
            <td>` + response['height'] + `</td>
            <td>` + response['mass'] + `</td>
            <td>` + response['hair_color'] + `</td>
            <td>` + response['skin_color'] + `</td>
            <td>` + response['eye_color'] + `</td>
            <td>` + response['birth_year'] + `</td>
            <td>` + response['gender'] + `</td>
          </tr>
          </tbody>

        </table>`
