function confirmDeleteImage(e, imageId) {
    e.preventDefault(); 

    Swal.fire({
        title: 'Você tem certeza?',
        text: `Deletar imagem com ID ${imageId}?`,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#172752',
        cancelButtonColor: '#c71e21',
        confirmButtonText: 'Sim',
        cancelButtonText: 'Não'
    }).then((result) => {
        if (result.isConfirmed) {

            document.getElementById(`delete-image-form-${imageId}`).submit();
        }
    });
}

const inputElement = document.querySelector('input[name="immobile"]');
const imagePreviewContainer = document.getElementById('image-preview-edit');

if (inputElement && imagePreviewContainer) {
    inputElement.addEventListener('change', function(event) {
        const files = event.target.files;
        imagePreviewContainer.innerHTML = ''; 

        for (const file of files) {
            const reader = new FileReader();
            reader.onload = function(e) {
                const img = document.createElement('img');
                img.src = e.target.result;
                img.className = 'h-40 w-40 object-cover rounded-md';

                const removeBtn = document.createElement('button');
                removeBtn.innerHTML = "<i class='bx bxs-trash-alt'></i>";
                removeBtn.className = "bg-red-700 px-2 py-1 rounded-md text-white font-semibold tracking-wide cursor-pointer text-sm absolute right-0 bottom-0";
                removeBtn.addEventListener('click', function() {
                    img.remove();
                    removeBtn.remove();
                    // Optionally, you could also remove the file from the input element here
                });

                const imgContainer = document.createElement('div');
                imgContainer.className = 'relative';
                imgContainer.appendChild(img);
                imgContainer.appendChild(removeBtn);

                imagePreviewContainer.appendChild(imgContainer);
            };
            reader.readAsDataURL(file);
        }
    });
}
