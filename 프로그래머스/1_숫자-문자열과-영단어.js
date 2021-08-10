function solution(s) {
    let arr = [/zero/g, /one/g, /two/g, /three/g, /four/g, /five/g, /six/g, /seven/g, /eight/g, /nine/g,  0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    for(let i = 0; i < 10; i++) {
        s = s.replace(arr[i], arr[10+i])
    }
    return s*1;
}