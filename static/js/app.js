var bLazy = new Blazy({
    selector: '.lazy, img',
    successClass: 'lazy-loaded',
    errorClass: 'lazy-error',
    error: function(ele, msg){
        if(msg === 'missing'){
            // Data-src is missing
            console.log(msg)
        }
        else if(msg === 'invalid'){
            // Data-src is invalid
            console.log(msg)
        }
    }
});