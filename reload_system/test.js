var random = Math.floor( Math.random() * (60-30)+30);
console.log( random );
setInterval(function() {
    //location.reload();
    console.log( random );
}, random*1000 );