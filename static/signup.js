const form = document.querySelector("#signup-form");

const checkPassword = () => {
  const pw1 = document.getElementById("password");
  const pw2 = document.getElementById("password2");
  if (pw1 === pw2) {
    return true;
  } else {
    return false;
  }
};

const handleSubmitSignup = async (event) => {
  event.preventDefault();
  const body = new FormData(form);
  const sha256Password = sha256(body.get("password"));
  body.set("password", sha256Password);
  if (checkPassword) {
    const res = await fetch("/signup", {
      method: "POST",
      body,
    });
    alert("회원가입에 성공했습니다.");
    window.location.pathname = "/login.html";
  } else {
    alert("비밀번호가 같지 않습니다.");
  }
};

form.addEventListener("submit", handleSubmitSignup);
