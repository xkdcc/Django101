$(document).ready(function () {

    // ++++++++++++++++++++ ajax_v1_demo_add_form ++++++++++++++++++++
    $('#ajax_v1_demo_add_form').on('submit', function (event) {
        event.preventDefault();
        console.log("ajax_v1_demo_add_form submitted!") // sanity check
        do_add_v1();
    });

    // AJAX for posting
    function do_add_v1() {
        console.log("add[post] is working!") // sanity check
        console.log($('input[name="v1_addend1"]').val())
        console.log($('input[name="v1_addend2"]').val())
        $.ajax({
            url: "/ajax/demo_ajax_v1_addition/", // the endpoint
            type: "POST", // http method
            data: {
                v1_addend1: $('input[name="v1_addend1"]').val(),
                v1_addend2: $('input[name="v1_addend2"]').val(),
            }, // data sent with the post request

            // handle a successful response
            success: function (data) {
                $('input[name="v1_results"]').val(''); // remove the value from the input
                console.log(data); // log the returned data to the console
                $('input[name="v1_results"]').val(data)
                console.log("success"); // another sanity check
            },

            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };

    // ++++++++++++++++++++ ajax_v2_demo_add_form ++++++++++++++++++++
    $('#ajax_v2_demo_add_form').on('submit', function (event) {
        event.preventDefault();
        console.log("ajax_v2_demo_add_form submitted!")  // sanity check
        do_add_v2();
    });

    // AJAX for posting
    function do_add_v2() {
        console.log("add[post] is working!") // sanity check
        console.log($('input[name="v2_addend1"]').val())
        console.log($('input[name="v2_addend2"]').val())
        $.ajax({
            url: "/ajax/demo_ajax_v2_addition/", // the endpoint
            type: "POST", // http method
            data: {
                v2_addend1: $('input[name="v2_addend1"]').val(),
                v2_addend2: $('input[name="v2_addend2"]').val(),
            }, // data sent with the post request

            // handle a successful response
            // Please note: 
            // Now in ajax v2 we're using "json" not "data" as in ajax v1!!!
            success: function (json) {
                $('input[name="v2_results"]').val(''); // remove the value from the input
                console.log(json); // log the returned json to the console
                $('input[name="v2_results"]').val(json.results)
                console.log("success"); // another sanity check
            },

            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };

    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


});