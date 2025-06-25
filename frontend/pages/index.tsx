import { useState } from "react";
import StoryForm from "../components/StoryForm";
import StoryViewer from "../components/StoryViewer";

export default function Home() {
  const [pages, setPages] = useState<any[]>([]);

  return (
    <div className="max-w-md mx-auto min-h-screen p-4">
      {!pages.length && <StoryForm onStoryGenerated={setPages} />}
      {pages.length > 0 && <StoryViewer pages={pages} />}
    </div>
  );
}
