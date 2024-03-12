const form = document.getElementById("login-form");

const handleSubmitLogin = async (event) => {
  event.preventDefault();
  const body = new FormData(form);
  const sha256password = sha256(body.get("password")); //패스워드 암호화
  body.set("password", sha256password); //암호화된 패스워드로 덮어씌움
  const res = await fetch("/login", {
    method: "POST",
    body,
  });

  alert("로그인 완료!");
  window.location.pathname = "/";
};

form.addEventListener("submit", handleSubmitLogin);
