const inputElement = document.querySelector('input[name="immobile"]');
const imagePreviewContainer = document.getElementById('image-preview-create');

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
