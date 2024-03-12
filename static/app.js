const form = document.querySelector("#content");

const handleSubmit = async (event) => {
  event.preventDefault();
  const body = new FormData(form);
  try {
    const res = await fetch("/games", {
      method: "POST",
      body,
    });
  } catch (e) {
    console.error(e);
  }
};

form.addEventListener("submit", handleSubmit);
