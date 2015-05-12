function triangleType(a, b, c){
    var arr = [a, b, c];
    for(var i = 0; i < arr.length - 1; i++){
        for(var j = i + 1; j < arr.length; j++){
            if(arr[i] > arr[j]){
                arr[i] = arr[i] + arr[j];
                arr[j] = arr[i] - arr[j];
                arr[i] = arr[i] - arr[j];
            }
        }
    }
    console.log(arr);
    if(arr[2] > arr[1] + arr[0]){
        return 0;
    }
    if(arr[2] * arr[2] > arr[1] * arr[1] + arr[0] * arr[0]){
        return 3;
    }else if(arr[2] * arr[2] == arr[1] * arr[1] + arr[0] * arr[0]){
        return 2;
    }else{
        return 1;
    }

}

console.log(triangleType(7,3,2));