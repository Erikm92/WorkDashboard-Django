
 function editurl() { 
    // Get the modal
        var modal = document.getElementById("myEditModal");
    
        // Get the button that opens the modal
        var btn = document.getElementById("myeditBtn");
    
        // Get the <span> element that closes the modal
        var span = document.getElementById("cancel");
    
        var done = document.getElementById("done");
        var removesrc = document.getElementById("none").href="javascript: void(0)";
        var removesrc = document.getElementById("none").target="";
        

       
    
        // When the user clicks the button, open the modal 
        btn.onclick = function() {
        modal.style.display = "block";
        }
    
        // When the user clicks on <span> (x), close the modal
        span.onclick = function() {
        modal.style.display = "none";
        window.location.reload();
        }
    
        done.onclick = function() {
        modal.style.display = "none";
            }
    
        // When the user clicks anywhere outside of the modal, close it
        window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
        }   
    }   