import { useState } from "react";

export default function StoryViewer({ pages }: { pages: { text: string; image: string }[] }) {
  const [index, setIndex] = useState(0);
  const next = () => setIndex(i => Math.min(i + 1, pages.length - 1));
  const prev = () => setIndex(i => Math.max(i - 1, 0));
  const page = pages[index];

  return (
    <div className="text-center space-y-4">
      <img src={page.image} alt="illustration" className="mx-auto rounded max-h-96 object-contain" />
      <p className="text-lg">{page.text}</p>
      <div className="flex justify-between">
        <button onClick={prev} className="bg-gray-300 px-4 py-2 rounded">⬅ Back</button>
        <button onClick={next} className="bg-green-600 text-white px-4 py-2 rounded">Next ➡</button>
      </div>
    </div>
  );
}
