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
    }).done(function(results) {
      // if (results.valid) {
      // }
      console.log(results)
    });
  });

  $('li.active').removeClass('active');

  if ($('#home').length) {
    $('#homeTab').addClass('active');
  } else if ($('#dashboard').length) {
    $('#dashboardTab').addClass('active');
  }
});
