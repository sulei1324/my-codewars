function validParentheses(parens){
    var t = [];
    for(var i = 0; i < parens.length; i++){
        console.log(t);
        if(parens[i] == '(' || i == 0 || t.length == 0){
            t.push(parens[i]);
        }else{
            if(t.pop() != '('){
                return false;
            }
        }
    }
    if(t.length != 0){
        return false;
    }
    return true;
}

console.log(validParentheses('(()'));