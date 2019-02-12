var config = {
    selectors: {
        add: '.basket-item-add',
        delete: '.basket-item-delete',
        quantity: '.basket-item-quantity'
    },
    urls: {
        add: '/basket/add/',
        update: '/basket/update/',
        delete: '/basket/remove/'
    }
};

function updateBasketItem(id) {
    // обновление селекторов по data-id
}


$(document).ready(function () {
    $(config.selectors.add).on('click', function () {
        var item_id = $(this).data('id');
        var item_url = config.urls.add + item_id + "/";

        var parent_item = $(this).parents()[0]; // <li>
        var counter = $(parent_item).find(config.selectors.quantity);

        $.ajax({
            url: item_url,

            success: function (data) {
                counter.text(data.quantity)
                // $(parent_item).hide();
            }
        });
    })
});