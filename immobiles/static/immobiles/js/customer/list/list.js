function confirmDeleteCustomer(e, form, name){
    e.preventDefault();

    Swal.fire({
        title: 'Você tem certeza?',
        text: `Deletar cliente - ${name}`,
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
