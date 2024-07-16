document.addEventListener('DOMContentLoaded', function () {

    const btnGrid = document.getElementById("btn-grid-immobile-item");
    const btnList = document.getElementById("btn-list-immobile-item");
    const viewGrid = document.getElementById("grid-view");
    const viewList = document.getElementById("list-view");

    function setView(view) {
        if (view === 'grid') {
            viewGrid.style.display = "block";
            viewList.style.display = "none";
            btnGrid.classList.add('active');
            btnList.classList.remove('active');
        } else {
            viewGrid.style.display = "none";
            viewList.style.display = "block";
            btnGrid.classList.remove('active');
            btnList.classList.add('active');
        }
        localStorage.setItem('immobileView', view);
    }

    btnGrid.addEventListener('click', function () {
        setView('grid');
    });

    btnList.addEventListener('click', function () {
        setView('list');
    });

    const savedView = localStorage.getItem('immobileView') || 'grid';
    setView(savedView);
});

function confirmDeleteImmobile(e, form, code, type){
    e.preventDefault();

    Swal.fire({
        title: 'Você tem certeza?',
        text: `Deletar imóvel com código ${code} do tipo ${type}`,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#172752',
        cancelButtonColor: '#c71e21',
        confirmButtonText: 'Sim',
        cancelButtonText: 'Não'
    }).then((result) => {
        if (result.isConfirmed) {
            form.submit();
        }
    });
}

function confirmCreate(event, form) {
    event.preventDefault();

    Swal.fire({
        title: 'Você tem certeza?',
        text: "Deseja realmente cadastrar?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#172752',
        cancelButtonColor: '#c71e21',
        confirmButtonText: 'Sim',
        cancelButtonText: 'Não'
    }).then((result) => {
        if (result.isConfirmed) {
            form.submit();

            Swal.fire({
                icon: 'success',
                title: 'Sucesso',
                text: 'Imóvel cadastrado com sucesso!',
            });
        }
    });
}