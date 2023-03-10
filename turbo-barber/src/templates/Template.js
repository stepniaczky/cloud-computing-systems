import Navbar from "../components/Navbar";

const Template = ({ children }) => (
  <div className="min-h-screen flex flex-col bg-gray-600">
    <Navbar />
    <div className="flex-grow max-w-screen-xl self-center w-full px-2 sm:px-4">
      {children}
    </div>
  </div>
);

export default Template;
