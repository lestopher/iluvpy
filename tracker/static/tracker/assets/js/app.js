function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));  
}

function setCsrfToken(csrf) {
  $.ajaxSetup({
    crossDomain: false,
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type)) {
        xhr.setRequestHeader("X-CSRFToken", csrf);
      }
    }
  });
}

$(document).ready(function() {
  $('#setGoalWeightBtn').on('click', function(ev) {
    $('#setGoalWeight').removeClass('hide');
  });

  $('#hideGoalMessageBtn').on('click', function(ev) {
    $(this).parent().removeClass('alert-success alert-error').addClass('hide')
      .find('#msg').text('');
  });

  $('#submitGoalWeight').on('click', function(ev) {
    var goalWeight = $('#goalWeightInput').val(),
        csrf       = $.cookie('csrftoken');

    setCsrfToken(csrf);
    
    $.ajax({
      url: '/tracker/setGoalWeight/',
      type: 'POST',
      cache: false,
      data: {
        goalWeight: goalWeight
      }
    }).done(function(response) {
      var $submitGoalMessage = $('#submitGoalMessage'),
          results            = response[0];

      if (results.valid) {
        $submitGoalMessage.addClass('alert-success').find('#msg')
          .text('Successfully updated goal weight.');

      } else {
        $submitGoalMessage.addClass('alert-error').find('#msg')
          .text('An error occured when updating your goal weight. Please try again.\n' + results.message);
      }

      $submitGoalMessage.removeClass('hide');
    });
  });

  $('li.active').removeClass('active');

  if ($('#home').length) {
    $('#homeTab').addClass('active');
  } else if ($('#dashboard').length) {
    $('#dashboardTab').addClass('active');
  }
});
