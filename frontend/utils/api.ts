import axios from "axios";

const API = axios.create({
  baseURL: "https://magic-branch.onrender.com", // Use Render backend URL
});

export const generateStory = async (payload: {
  name: string;
  age: number;
  interests: string[];
  length: number;
}) => {
  const res = await API.post("/generate", payload);
  return res.data.pages;
};
