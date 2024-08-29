let headers = {
  // 불법으로 js를 수정하여 하는 임의적인 공격을 방지하는 보안 처리
  "X-CSRFToken": getCookie("csrftoken"),
};
const axiosInstance = axios.create({
  baseURL: "/",
  headers: headers,
});
