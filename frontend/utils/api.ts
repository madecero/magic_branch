import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000", // Update if backend URL changes
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
