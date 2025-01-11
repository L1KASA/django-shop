document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".add-to-cart");
    const cartCount = document.getElementById("cart-count");

    buttons.forEach((button) => {
        button.addEventListener("click", function () {

            const productId = button.getAttribute("data-product-id");

            fetch(`/cart/add/${productId}/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": document.cookie.match(/csrftoken=([^;]+)/)[1],
                },
            })

                .then((response) => {
                    if (response.status === 401) {
                        alert("You must log in to add items to the cart.");
                        return;
                    }
                    return response.json();
                })
                .then(({cart_count, message}) => {
                    if (cart_count !== undefined) {
                        cartCount.textContent = cart_count;
                        alert(message);
                    }
                })
                .catch(console.error);
        });
    });
});