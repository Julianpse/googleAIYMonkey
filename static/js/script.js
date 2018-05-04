$(document).ready(function() {
  showOpenTasks(openTaskObject);
  showClosedTasks(closedTaskObject);
  changeStatus();
  deleteFromList();
});

var openTasks = {{open_tasks | jsonvalue | safe}};
var openTaskObject = JSON.parse(openTasks);

var closedTasks = {{closed_tasks | jsonvalue | safe }};
var closedTaskObject = JSON.parse(closedTasks);


// These two functions below load all of the tasks in the database
function showOpenTasks(openTaskObject){
  var task = [];
  openTaskObject.forEach(function(element){
    $("#todoList").append(`<li><div data-status="${element[2]}" data-id="${element[0]}" class="card ${element[2]}" id="${element[0]}">${element[1]}
      <h6 class = "x-icon" id="${element[0]}">x</h6>
  </div></li>`);
  });
}

function showClosedTasks(closedTaskObject){
  var task = [];
  closedTaskObject.forEach(function(element){
    $("#completedList").append(`<li><div data-status="${element[2]}" data-id="${element[0]}" class="card ${element[2]}" id="${element[0]}">${element[1]}
      <h6 class = "x-icon" id="${element[0]}">x</h6>
    </div></li>`);
  });
}


//Changes status between todo and completed
function changeStatus(){
  var clicks = 0;
  if (clicks == 0) {
    $('.card').click(function(event){
      event.stopPropagation();
      event.stopImmediatePropagation();
      if($(this).hasClass("card open")){
        $(this).appendTo("#completedList");
        $(this).attr("class","card closed");

      } else if ($(this).hasClass("card closed")) {
        $(this).appendTo("#todoList");
        $(this).attr("class","card open");
      }
        var objectID = $(this)[0].id;
        clicks ++;
        ajaxPost(objectID);
    });
  }
}


//Bug happening where the change status function is getting called instead
function deleteFromList(){
  $('.x-icon').click(function(e){
      e.stopPropagation();
      confirm("Are you sure you want to remove this from your list?");
        $(this).parent().remove();
        console.log($(this));
        var objectID = $(this)[0].id;
        console.log(objectID);
        ajaxPostDelete(objectID);
  });
}

//ajax post status
function ajaxPost(param){
  $.ajax("/status", {
    data: JSON.stringify(param),
    type: 'POST',
    contentType: 'application/json'
  });
}

//ajax post delete
function ajaxPostDelete(param){
  $.ajax("/deleted", {
    data: JSON.stringify(param),
    type: 'POST',
    contentType: 'application/json'
  });
}
