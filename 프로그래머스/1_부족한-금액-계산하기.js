function solution(price, money, count) {
    let sum = 0;
    for(let i = 1; i<= count; i++) money -= price*i;
    return money >= 0 ? 0 : Math.abs(money);
}