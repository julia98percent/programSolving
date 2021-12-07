function set_award(n) {
  switch (n) {
    case 6:
      return 1;
    case 5:
      return 2;
    case 4:
      return 3;
    case 3:
      return 4;
    case 2:
      return 5;
    default:
      return 6;
  }
}
function solution(l, w) {
  //매개변수 l에서의 0 개수
  let num_zero = l.filter((item) => item == 0).length;

  // l과 w 병합 (정렬 및 중복제거)
  let result = [...l, ...w].sort();
  let filtered_result = result.filter(
    (item, idx) => item > 0 && result.indexOf(item) === idx
  );
  //당첨된 숫자 개수 = l+w의 길이 - 중복제거된 l+w 길이 - 0의 개수
  let num_win = result.length - filtered_result.length - num_zero;
  return [set_award(num_win + num_zero), set_award(num_win)];
}
