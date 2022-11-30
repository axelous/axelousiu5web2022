import { Route, Routes } from "react-router-dom";
import {HomePage} from "./pages/HomePage";
import {ProfilePage} from "./pages/ProfilePage";
import {PostPage} from "./pages/PostPage";

export const App = () =>{

    return (
        <Routes>
            <Route path="/" element={<HomePage />}/>
            <Route path="/profile/:idUser" element={<ProfilePage />}/>
            <Route path="/post/:idPost" element={<PostPage />}/>
        </Routes>
    )
}

