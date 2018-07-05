let dom = {
    showResidentsData(residents) {
        let content = document.getElementById("resident-data");

        residents.forEach(function (resident) {
            function reqListener() {
                if (getResident.status < 400) {
                    let resident = JSON.parse(this.response);

                    let row = content.insertRow();
                    let name = row.insertCell(0);
                    let height = row.insertCell(1);
                    let mass = row.insertCell(2);
                    let skin = row.insertCell(3);
                    let hair = row.insertCell(4);
                    let eye = row.insertCell(5);
                    let birth = row.insertCell(6);
                    let gender = row.insertCell(7);

                    name.innerHTML = resident.name;
                    height.innerHTML = resident.height;
                    mass.innerHTML = resident.mass;
                    skin.innerHTML = resident.skin_color;
                    hair.innerHTML = resident.hair_color;
                    eye.innerHTML = resident.eye_color;
                    birth.innerHTML = resident.birth_year;
                    gender.innerHTML = resident.gender;


                }
            }

            let getResident = new XMLHttpRequest();
            getResident.addEventListener('load', reqListener);
            getResident.open('GET', resident);
            getResident.send();
        })
    },
    getModal() {
        let url = this.dataset.url;
        let modal = document.getElementById('modal');
        let span = document.getElementsByClassName("close")[0];

        let content = document.getElementById("resident-data");
        content.innerHTML = "<thead> <tr></tr> </thead>";

        $("#resident-data>thead>tr").append("<th>Name</th>");
        $("#resident-data>thead>tr").append("<th>Height</th>");
        $("#resident-data>thead>tr").append("<th>Mass</th>");
        $("#resident-data>thead>tr").append("<th>Skin color</th>");
        $("#resident-data>thead>tr").append("<th>Hair color</th>");
        $("#resident-data>thead>tr").append("<th>Eye color</th>");
        $("#resident-data>thead>tr").append("<th>Birth Year</th>");
        $("#resident-data>thead>tr").append("<th>Gender</th>");
        modal.style.display = "block";
        span.addEventListener("click", function () {
            modal.style.display = "none";
        });

        function reqListener() {
            if (getResidents.status < 400) {
                let residents = JSON.parse(this.response).residents;
                dom.showResidentsData(residents);
            }
        }

        let getResidents = new XMLHttpRequest();
        getResidents.addEventListener('load', reqListener);
        getResidents.open('GET', url);
        getResidents.send();


    },
    initialize() {
        let buttons = document.getElementsByClassName('details');

        [].forEach.call(buttons, function (button) {
            button.addEventListener("click", dom.getModal);
        });
        window.addEventListener("click", function (event) {
            if (event.target === modal) {
                modal.style.display = "none";
            }
        })
    }
};

dom.initialize();