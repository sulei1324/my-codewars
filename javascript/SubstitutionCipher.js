function SubstitutionCipher(abc1, abc2){
    var abcA1 = abc1.split('');
    var abcA2 = abc2.split('');
    this.encode = function(str){
        var sA = str.split('');
        var rA = sA.map(function(v){
            var i = abcA1.indexOf(v);
            if(i == -1){
                return v;
            }
            else{
                return abcA2[i];
            }
        });
        return rA.join('');
    };
    this.decode = function(str){
        var sA = str.split('');
        var rA = sA.map(function(v){
            var i = abcA2.indexOf(v);
            if(i == -1){
                return v;
            }
            else{
                return abcA1[i];
            }
        });
        return rA.join('');
    };
}

abc1 = 'abcdefghijklmnopqrstuvwxyz';
abc2 = 'etaoinshrdlucmfwypvbgkjqxz';
var sub = new SubstitutionCipher(abc1, abc2);
console.log(sub.encode('abcdey'));

