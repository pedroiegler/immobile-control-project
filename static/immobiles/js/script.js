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