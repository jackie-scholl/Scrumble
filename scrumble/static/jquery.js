$(document).ready(function() {  
  $(".selectcheck").click(function (e) {
        var cb = $(this).find(":checkbox")[0];
        if (e.target != cb) cb.checked = !cb.checked;
        $(this).toggleClass("selected", cb.checked);
    });
  
  $(".new-card-save").click(function () {
      var objective = document.getElementById("objective-input").value; 
      var task = document.getElementById("task-input").value;
      $("#addnew").prepend("<li class='list-group-item'> objective: " + objective + "<div class='dropdown pull-right no-padding'><button class='btn btn-default dropdown-toggle' type='button' id='dropdownMenu1' data-toggle='dropdown' aria-haspopup='true' aria-expanded='true'>Assign To<span class='caret'></span></button><ul class='dropdown-menu' aria-labelledby='dropdownMenu1'><li><a href='#'><input class='selectall' type='checkbox' /> Select All</a></li><li><a href='#'><input class='checkbox1' type='checkbox' /> Group 1</a></li><li><a href='#'><input class='checkbox1' type='checkbox' /> Group 2</a></li><li><a href='#'><input class='checkbox1' type='checkbox' /> Group 3</a></li><li><a href='#'><input class='checkbox1' type='checkbox' /> Group 4</a></li></ul></div><br> task: " + task + "</li>")
  });
  
  $(".new-project-card-save").click(function () {
      var task = document.getElementById("project-task-input").value;
      $("#addnew").prepend("<li class='list-group-item'> task: " + task + "</li>")
  });
  
});