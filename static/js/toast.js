// GLOBAL VARIABLES
let currentDeleteId = null;

// UTILITY FUNCTIONS
// Fungsi untuk mendapatkan CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// LOADING STATE FUNCTIONS
function showLoading() {
    const loading = document.getElementById('loading');
    const productList = document.getElementById('productList');
    const empty = document.getElementById('empty');
    const error = document.getElementById('error');
    
    if (loading) loading.classList.remove('hidden');
    if (productList) productList.classList.add('hidden');
    if (empty) empty.classList.add('hidden');
    if (error) error.classList.add('hidden');
}

function hideLoading() {
    const loading = document.getElementById('loading');
    if (loading) loading.classList.add('hidden');
}

// TOAST FUNCTIONS
function showToast(message, type = 'success') {
    const toast = document.getElementById('toast');
    const toastMessage = document.getElementById('toastMessage');
    const toastIcon = document.getElementById('toastIcon');
    
    if (!toast || !toastMessage) return;
    
    toastMessage.textContent = message;
    
    toast.classList.remove('bg-green-500', 'bg-red-500', 'bg-blue-500', 'bg-yellow-500', 'hidden');
    
    if (type === 'success') {
        toast.classList.add('bg-green-500', 'text-white');
        if (toastIcon) toastIcon.innerHTML = '✓';
    } else if (type === 'error') {
        toast.classList.add('bg-red-500', 'text-white');
        if (toastIcon) toastIcon.innerHTML = '✕';
    } else if (type === 'warning') {
        toast.classList.add('bg-yellow-500', 'text-white');
        if (toastIcon) toastIcon.innerHTML = '⚠';
    } else {
        toast.classList.add('bg-blue-500', 'text-white');
        if (toastIcon) toastIcon.innerHTML = 'ℹ';
    }

    setTimeout(() => {
        toast.classList.add('hidden');
    }, 3000);
}

// MODAL FUNCTIONS - CREATE
function showCreateModal() {
    const modal = document.getElementById('createProductModal');
    if (modal) {
        modal.classList.remove('hidden');
        document.getElementById('createProductForm').reset();
    }
}

function closeCreateModal() {
    const modal = document.getElementById('createProductModal');
    if (modal) {
        modal.classList.add('hidden');
    }
}

// MODAL FUNCTIONS - UPDATE
function showUpdateModal(id, name, price, description, thumbnail, category, is_featured, stock) {
    const modal = document.getElementById('updateProductModal');
    if (modal) {
        modal.classList.remove('hidden');
        document.getElementById('update_product_id').value = id;
        document.getElementById('update_name').value = name;
        document.getElementById('update_price').value = price;
        document.getElementById('update_description').value = description;
        document.getElementById('update_thumbnail').value = thumbnail || '';
        document.getElementById('update_category').value = category || '';
        document.getElementById('update_is_featured').checked = is_featured;
        document.getElementById('update_stock').value = stock;
    }
}

function closeUpdateModal() {
    const modal = document.getElementById('updateProductModal');
    if (modal) {
        modal.classList.add('hidden');
    }
}

// MODAL FUNCTIONS - DELETE
function showDeleteModal(id) {
    currentDeleteId = id;
    const modal = document.getElementById('deleteConfirmModal');
    if (modal) {
        modal.classList.remove('hidden');
    }
}

function closeDeleteModal() {
    const modal = document.getElementById('deleteConfirmModal');
    if (modal) {
        modal.classList.add('hidden');
    }
    currentDeleteId = null;
}

// FETCH AND DISPLAY PRODUCTS
async function refreshProducts() {
    showLoading();
    
    try {
        const response = await fetch('/json/');
        
        if (!response.ok) {
            throw new Error('Gagal memuat data');
        }
        
        const products = await response.json();
        
        hideLoading();
        
        const productList = document.getElementById('productList');
        const empty = document.getElementById('empty');
        
        if (!productList) return;
        
        productList.innerHTML = '';
        
        if (products.length === 0) {
            if (empty) empty.classList.remove('hidden');
            return;
        }

        productList.classList.remove('hidden');
        
        products.forEach(item => {
            const product = item.fields;
            const id = item.pk;
            
            const escapedName = (product.name || '').replace(/'/g, "\\'").replace(/"/g, '&quot;');
            const escapedDesc = (product.description || '').replace(/'/g, "\\'").replace(/"/g, '&quot;');
            const escapedThumb = (product.thumbnail || '').replace(/'/g, "\\'").replace(/"/g, '&quot;');
            const escapedCategory = (product.category || '').replace(/'/g, "\\'").replace(/"/g, '&quot;');
            
            const categoryDisplay = product.category ? product.category.split(' ').map(word => 
                word.charAt(0).toUpperCase() + word.slice(1)
            ).join(' ') : '';
            
            const card = `
                <div class="bg-white rounded-lg shadow-md hover:shadow-lg transition p-4">
                    ${product.thumbnail ? `
                        <img src="${product.thumbnail}" alt="${product.name}" class="w-full h-48 object-cover rounded-lg mb-3">
                    ` : `
                        <div class="w-full h-48 bg-gray-200 rounded-lg mb-3 flex items-center justify-center">
                            <span class="text-gray-400">No Image</span>
                        </div>
                    `}
                    
                    ${product.is_featured ? '<span class="inline-block bg-yellow-400 text-yellow-900 text-xs px-2 py-1 rounded mb-2">⭐ Featured</span>' : ''}
                    
                    <h3 class="font-bold text-lg mb-1">${product.name}</h3>
                    
                    ${product.category ? `<p class="text-sm text-gray-500 mb-2">📁 ${categoryDisplay}</p>` : ''}
                    
                    <p class="text-blue-600 font-semibold text-xl mb-2">Rp ${parseInt(product.price).toLocaleString('id-ID')}</p>
                    
                    <p class="text-sm text-gray-600 mb-3 line-clamp-2">${product.description}</p>
                    
                    <p class="text-sm mb-3">
                        <span class="font-medium">Stock:</span> 
                        <span class="${product.stock > 0 ? 'text-green-600' : 'text-red-600'} font-semibold">${product.stock}</span>
                    </p>
                    
                    <p class="text-xs text-gray-400 mb-4">
                        👁️ ${product.product_views || 0} views
                    </p>
                    
                    <div class="flex gap-2">
                        <button onclick='showUpdateModal("${id}", "${escapedName}", ${product.price}, "${escapedDesc}", "${escapedThumb}", "${escapedCategory}", ${product.is_featured}, ${product.stock})' 
                                class="flex-1 bg-yellow-500 text-white px-3 py-2 rounded hover:bg-yellow-600 transition text-sm font-medium">
                            ✏️ Edit
                        </button>
                        <button onclick='showDeleteModal("${id}")' 
                                class="flex-1 bg-red-500 text-white px-3 py-2 rounded hover:bg-red-600 transition text-sm font-medium">
                            🗑️ Hapus
                        </button>
                    </div>
                </div>
            `;
            productList.innerHTML += card;
        });
        
    } catch (error) {
        hideLoading();
        const errorDiv = document.getElementById('error');
        if (errorDiv) errorDiv.classList.remove('hidden');
        console.error('Error:', error);
        showToast('Gagal memuat data product', 'error');
    }
}

// CREATE PRODUCT
document.addEventListener('DOMContentLoaded', function() {
    const createForm = document.getElementById('createProductForm');
    
    if (createForm) {
        createForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            
            try {
                const response = await fetch('/create-ajax/', {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken')
                    }
                });
                
                const data = await response.json();
                
                if (response.ok && data.status === 'success') {
                    showToast(data.message, 'success');
                    closeCreateModal();
                    await refreshProducts(); 
                } else {
                    showToast(data.message || 'Gagal menambahkan product', 'error');
                }
            } catch (error) {
                showToast('Terjadi kesalahan saat menambahkan product', 'error');
                console.error('Error:', error);
            }
        });
    }
});

// EDIT PRODUCT
document.addEventListener('DOMContentLoaded', function() {
    const updateForm = document.getElementById('updateProductForm');
    
    if (updateForm) {
        updateForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const id = document.getElementById('update_product_id').value;
            const formData = new FormData(this);
            
            try {
                const response = await fetch(`/update-ajax/${id}/`, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken')
                    }
                });
                
                const data = await response.json();
                
                if (response.ok && data.status === 'success') {
                    showToast(data.message, 'success');
                    closeUpdateModal();
                    await refreshProducts(); 
                } else {
                    showToast(data.message || 'Gagal mengupdate product', 'error');
                }
            } catch (error) {
                showToast('Terjadi kesalahan saat mengupdate product', 'error');
                console.error('Error:', error);
            }
        });
    }
});

// DELETE PRODUCT
async function confirmDelete() {
    if (!currentDeleteId) return;
    
    try {
        const response = await fetch(`/delete-ajax/${currentDeleteId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        });
        
        const data = await response.json();
        
        if (response.ok && data.status === 'success') {
            showToast(data.message, 'success');
            closeDeleteModal();
            await refreshProducts(); 
        } else {
            showToast(data.message || 'Gagal menghapus product', 'error');
        }
    } catch (error) {
        showToast('Terjadi kesalahan saat menghapus product', 'error');
        console.error('Error:', error);
    }
}


// LOAD PRODUCTS
document.addEventListener('DOMContentLoaded', function() {
    refreshProducts();
});

// Close modal when clicking outside
window.onclick = function(event) {
    const modals = ['createProductModal', 'updateProductModal', 'deleteConfirmModal'];
    modals.forEach(modalId => {
        const modal = document.getElementById(modalId);
        if (event.target === modal) {
            modal.classList.add('hidden');
        }
    });
}