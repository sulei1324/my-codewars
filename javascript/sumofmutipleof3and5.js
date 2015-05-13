function solution(number){
    var s = 0;
    for(var i = 0; i < number; i++){
        if( i%3 == 0 || i%5 == 0 ){
            s += i;
        }
    }
    return s;
}

console.log(solution(10));